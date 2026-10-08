"""Service module 9890: business logic, no crypto."""


def calculate_total_9890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9890():
    return 'module 9890 handles orders and invoices'
