"""Service module 15153: business logic, no crypto."""


def calculate_total_15153(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15153():
    return 'module 15153 handles orders and invoices'
