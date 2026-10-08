"""Service module 20968: business logic, no crypto."""


def calculate_total_20968(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20968():
    return 'module 20968 handles orders and invoices'
