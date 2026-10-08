"""Service module 10254: business logic, no crypto."""


def calculate_total_10254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10254():
    return 'module 10254 handles orders and invoices'
