"""Service module 45397: business logic, no crypto."""


def calculate_total_45397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45397():
    return 'module 45397 handles orders and invoices'
