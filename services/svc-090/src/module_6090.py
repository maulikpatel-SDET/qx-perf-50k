"""Service module 6090: business logic, no crypto."""


def calculate_total_6090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6090():
    return 'module 6090 handles orders and invoices'
