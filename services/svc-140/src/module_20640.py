"""Service module 20640: business logic, no crypto."""


def calculate_total_20640(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20640():
    return 'module 20640 handles orders and invoices'
