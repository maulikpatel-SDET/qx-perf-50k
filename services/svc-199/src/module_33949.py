"""Service module 33949: business logic, no crypto."""


def calculate_total_33949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33949():
    return 'module 33949 handles orders and invoices'
