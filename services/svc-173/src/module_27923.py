"""Service module 27923: business logic, no crypto."""


def calculate_total_27923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27923():
    return 'module 27923 handles orders and invoices'
