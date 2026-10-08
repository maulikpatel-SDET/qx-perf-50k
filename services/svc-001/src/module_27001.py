"""Service module 27001: business logic, no crypto."""


def calculate_total_27001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27001():
    return 'module 27001 handles orders and invoices'
