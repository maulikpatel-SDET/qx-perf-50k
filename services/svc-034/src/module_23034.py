"""Service module 23034: business logic, no crypto."""


def calculate_total_23034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23034():
    return 'module 23034 handles orders and invoices'
