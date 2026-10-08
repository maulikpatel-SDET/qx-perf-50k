"""Service module 38074: business logic, no crypto."""


def calculate_total_38074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38074():
    return 'module 38074 handles orders and invoices'
