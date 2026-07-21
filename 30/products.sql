CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    Quantity INT NOT NULL CHECK (Quantity >= 0),
    Status VARCHAR(20) NULL
);
GO

CREATE OR ALTER PROCEDURE DecreaseProductQuantity
    @ProductID INT,
    @Quantity INT
AS
BEGIN
    SET NOCOUNT ON;

    IF @Quantity <= 0
    BEGIN
        THROW 50001, 'Quantity must be greater than 0.', 1;
    END;

    UPDATE Products
    SET Quantity = Quantity - @Quantity
    WHERE ProductID = @ProductID
      AND Quantity >= @Quantity;

    IF @@ROWCOUNT = 0
    BEGIN
        THROW 50002, 'Product was not found or does not have enough quantity.', 1;
    END;
END;
GO

CREATE OR ALTER TRIGGER trg_SetProductStatus
ON Products
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE p
    SET Status =
        CASE
            WHEN p.Quantity = 0 THEN 'out of stock'
            WHEN p.Quantity BETWEEN 1 AND 10 THEN 'low stock'
            WHEN p.Quantity > 10 THEN 'in stock'
        END
    FROM Products AS p
    INNER JOIN inserted AS i
        ON p.ProductID = i.ProductID
    WHERE ISNULL(p.Status, '') <>
        CASE
            WHEN p.Quantity = 0 THEN 'out of stock'
            WHEN p.Quantity BETWEEN 1 AND 10 THEN 'low stock'
            WHEN p.Quantity > 10 THEN 'in stock'
        END;
END;
GO

INSERT INTO Products (ProductID, ProductName, Price, Quantity)
VALUES
    (1, N'Laptop', 2500.00, 15),
    (2, N'Mouse', 35.00, 8),
    (3, N'Keyboard', 80.00, 10),
    (4, N'Monitor', 650.00, 0),
    (5, N'Headphones', 120.00, 25);
GO

EXEC DecreaseProductQuantity @ProductID = 1, @Quantity = 5;
GO

SELECT *
FROM Products;
