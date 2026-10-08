"""Service module 18515: business logic, no crypto."""


def calculate_total_18515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18515():
    return 'module 18515 handles orders and invoices'
