"""Service module 27328: business logic, no crypto."""


def calculate_total_27328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27328():
    return 'module 27328 handles orders and invoices'
