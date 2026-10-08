"""Service module 48071: business logic, no crypto."""


def calculate_total_48071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48071():
    return 'module 48071 handles orders and invoices'
