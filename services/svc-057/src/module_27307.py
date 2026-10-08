"""Service module 27307: business logic, no crypto."""


def calculate_total_27307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27307():
    return 'module 27307 handles orders and invoices'
