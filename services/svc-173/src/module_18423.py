"""Service module 18423: business logic, no crypto."""


def calculate_total_18423(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18423():
    return 'module 18423 handles orders and invoices'
