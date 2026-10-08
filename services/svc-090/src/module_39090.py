"""Service module 39090: business logic, no crypto."""


def calculate_total_39090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39090():
    return 'module 39090 handles orders and invoices'
