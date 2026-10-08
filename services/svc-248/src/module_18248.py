"""Service module 18248: business logic, no crypto."""


def calculate_total_18248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18248():
    return 'module 18248 handles orders and invoices'
