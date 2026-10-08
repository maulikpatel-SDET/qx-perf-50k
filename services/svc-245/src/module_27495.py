"""Service module 27495: business logic, no crypto."""


def calculate_total_27495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27495():
    return 'module 27495 handles orders and invoices'
