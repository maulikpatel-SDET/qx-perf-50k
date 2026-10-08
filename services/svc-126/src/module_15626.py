"""Service module 15626: business logic, no crypto."""


def calculate_total_15626(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15626():
    return 'module 15626 handles orders and invoices'
