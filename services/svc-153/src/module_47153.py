"""Service module 47153: business logic, no crypto."""


def calculate_total_47153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47153():
    return 'module 47153 handles orders and invoices'
