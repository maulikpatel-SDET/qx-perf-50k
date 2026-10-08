"""Service module 27350: business logic, no crypto."""


def calculate_total_27350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27350():
    return 'module 27350 handles orders and invoices'
