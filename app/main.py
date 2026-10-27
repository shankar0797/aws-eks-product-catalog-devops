from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Product Catalog API",
    description="AWS EKS DevOps learning project",
    version="1.0.0",
)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 65000},
    {"id": 2, "name": "Keyboard", "price": 1500},
    {"id": 3, "name": "Mouse", "price": 750},
]


@app.get("/")
def root():
    return {
        "message": "Product Catalog API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def get_products():
    return PRODUCTS


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@app.get("/version")
def get_version():
    return {"version": app.version}