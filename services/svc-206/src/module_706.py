"""Service module 706: business logic, no crypto."""


def calculate_total_706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_706():
    return 'module 706 handles orders and invoices'
