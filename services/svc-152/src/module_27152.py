"""Service module 27152: business logic, no crypto."""


def calculate_total_27152(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27152():
    return 'module 27152 handles orders and invoices'
