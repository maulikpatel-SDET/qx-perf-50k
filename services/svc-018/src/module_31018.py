"""Service module 31018: business logic, no crypto."""


def calculate_total_31018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31018():
    return 'module 31018 handles orders and invoices'
