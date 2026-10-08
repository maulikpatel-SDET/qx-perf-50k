"""Service module 19581: business logic, no crypto."""


def calculate_total_19581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19581():
    return 'module 19581 handles orders and invoices'
