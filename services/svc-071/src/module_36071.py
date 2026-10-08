"""Service module 36071: business logic, no crypto."""


def calculate_total_36071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36071():
    return 'module 36071 handles orders and invoices'
