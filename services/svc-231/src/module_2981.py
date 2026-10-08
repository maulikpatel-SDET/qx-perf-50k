"""Service module 2981: business logic, no crypto."""


def calculate_total_2981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2981():
    return 'module 2981 handles orders and invoices'
