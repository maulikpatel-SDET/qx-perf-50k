"""Service module 45602: business logic, no crypto."""


def calculate_total_45602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45602():
    return 'module 45602 handles orders and invoices'
