"""Service module 27645: business logic, no crypto."""


def calculate_total_27645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27645():
    return 'module 27645 handles orders and invoices'
