"""Service module 27008: business logic, no crypto."""


def calculate_total_27008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27008():
    return 'module 27008 handles orders and invoices'
