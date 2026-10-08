"""Service module 44439: business logic, no crypto."""


def calculate_total_44439(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44439():
    return 'module 44439 handles orders and invoices'
