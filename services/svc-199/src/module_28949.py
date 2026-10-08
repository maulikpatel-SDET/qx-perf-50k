"""Service module 28949: business logic, no crypto."""


def calculate_total_28949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28949():
    return 'module 28949 handles orders and invoices'
