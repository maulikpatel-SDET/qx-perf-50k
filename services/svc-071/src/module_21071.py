"""Service module 21071: business logic, no crypto."""


def calculate_total_21071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21071():
    return 'module 21071 handles orders and invoices'
