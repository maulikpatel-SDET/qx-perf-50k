"""Service module 35589: business logic, no crypto."""


def calculate_total_35589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35589():
    return 'module 35589 handles orders and invoices'
