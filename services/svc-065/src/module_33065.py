"""Service module 33065: business logic, no crypto."""


def calculate_total_33065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33065():
    return 'module 33065 handles orders and invoices'
