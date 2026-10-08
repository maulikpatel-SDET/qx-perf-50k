"""Service module 27831: business logic, no crypto."""


def calculate_total_27831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27831():
    return 'module 27831 handles orders and invoices'
