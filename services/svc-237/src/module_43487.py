"""Service module 43487: business logic, no crypto."""


def calculate_total_43487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43487():
    return 'module 43487 handles orders and invoices'
