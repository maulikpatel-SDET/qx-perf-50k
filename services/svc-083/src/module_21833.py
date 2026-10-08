"""Service module 21833: business logic, no crypto."""


def calculate_total_21833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21833():
    return 'module 21833 handles orders and invoices'
