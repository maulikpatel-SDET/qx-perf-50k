"""Service module 26246: business logic, no crypto."""


def calculate_total_26246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26246():
    return 'module 26246 handles orders and invoices'
