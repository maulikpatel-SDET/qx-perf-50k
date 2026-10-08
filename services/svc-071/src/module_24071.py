"""Service module 24071: business logic, no crypto."""


def calculate_total_24071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24071():
    return 'module 24071 handles orders and invoices'
