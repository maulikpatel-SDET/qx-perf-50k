"""Service module 38071: business logic, no crypto."""


def calculate_total_38071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38071():
    return 'module 38071 handles orders and invoices'
