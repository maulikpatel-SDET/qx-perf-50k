"""Service module 47420: business logic, no crypto."""


def calculate_total_47420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47420():
    return 'module 47420 handles orders and invoices'
