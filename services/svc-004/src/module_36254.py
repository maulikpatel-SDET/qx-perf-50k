"""Service module 36254: business logic, no crypto."""


def calculate_total_36254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36254():
    return 'module 36254 handles orders and invoices'
