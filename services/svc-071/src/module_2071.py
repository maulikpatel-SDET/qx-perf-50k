"""Service module 2071: business logic, no crypto."""


def calculate_total_2071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2071():
    return 'module 2071 handles orders and invoices'
