"""Service module 27268: business logic, no crypto."""


def calculate_total_27268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27268():
    return 'module 27268 handles orders and invoices'
