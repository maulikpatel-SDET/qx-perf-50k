"""Service module 46975: business logic, no crypto."""


def calculate_total_46975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46975():
    return 'module 46975 handles orders and invoices'
