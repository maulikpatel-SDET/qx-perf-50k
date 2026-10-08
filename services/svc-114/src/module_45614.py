"""Service module 45614: business logic, no crypto."""


def calculate_total_45614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45614():
    return 'module 45614 handles orders and invoices'
