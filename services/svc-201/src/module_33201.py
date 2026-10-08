"""Service module 33201: business logic, no crypto."""


def calculate_total_33201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33201():
    return 'module 33201 handles orders and invoices'
