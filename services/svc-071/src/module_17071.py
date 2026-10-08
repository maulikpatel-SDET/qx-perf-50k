"""Service module 17071: business logic, no crypto."""


def calculate_total_17071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17071():
    return 'module 17071 handles orders and invoices'
