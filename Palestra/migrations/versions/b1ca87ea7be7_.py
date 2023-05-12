"""empty message

Revision ID: b1ca87ea7be7
Revises: ef2414ac614e
Create Date: 2021-05-04 18:05:22.524134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1ca87ea7be7'
down_revision = 'ef2414ac614e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abbonamenti',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.Enum('one', 'two', 'three', 'four', name='abbonamentot'), nullable=True),
    sa.Column('costo', sa.REAL(), nullable=True),
    sa.CheckConstraint('"costo" > 0'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('giorni',
    sa.Column('data', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('data')
    )
    op.create_table('salepesi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dimensione', sa.Integer(), nullable=True),
    sa.CheckConstraint('"dimensione" > 0'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stanze',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dimensione', sa.Integer(), nullable=True),
    sa.CheckConstraint('"dimensione" > 0'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('altri',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['utenti.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clienti',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['utenti.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('istruttori',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['utenti.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personeMax', sa.Integer(), nullable=True),
    sa.Column('giorno', sa.Date(), nullable=False),
    sa.Column('oraInizio', sa.DateTime(), nullable=True),
    sa.Column('oraFine', sa.DateTime(), nullable=True),
    sa.CheckConstraint('"oraFine"> "oraInizio"'),
    sa.ForeignKeyConstraint(['giorno'], ['giorni.data'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('abbonati',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('abbonamento', sa.Integer(), nullable=False),
    sa.Column('dataInizioAbbonamento', sa.Date(), nullable=True),
    sa.Column('dataFineAbbonamento', sa.Date(), nullable=True),
    sa.CheckConstraint('"dataFineAbbonamento" > "dataInizioAbbonamento"'),
    sa.ForeignKeyConstraint(['abbonamento'], ['abbonamenti.id'], ),
    sa.ForeignKeyConstraint(['id'], ['clienti.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('corsi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('iscrittiMax', sa.Integer(), nullable=True),
    sa.Column('istruttore', sa.Integer(), nullable=False),
    sa.Column('stanza', sa.Integer(), nullable=False),
    sa.CheckConstraint('"iscrittiMax" > 0'),
    sa.ForeignKeyConstraint(['istruttore'], ['istruttori.id'], ),
    sa.ForeignKeyConstraint(['stanza'], ['stanze.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nonabbonati',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['clienti.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salepesislot',
    sa.Column('salaPesi', sa.Integer(), nullable=False),
    sa.Column('slot', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['salaPesi'], ['salepesi.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['slot'], ['slot.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('salaPesi', 'slot')
    )
    op.create_table('corsislot',
    sa.Column('corso', sa.Integer(), nullable=False),
    sa.Column('slot', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['corso'], ['corsi.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['slot'], ['slot.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('corso', 'slot')
    )
    op.create_table('prenotazioni',
    sa.Column('abbonato', sa.Integer(), nullable=False),
    sa.Column('slot', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['abbonato'], ['abbonati.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['slot'], ['slot.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('abbonato', 'slot')
    )
    op.create_table('sedute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('corso', sa.Integer(), nullable=False),
    sa.Column('dataSeduta', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['corso'], ['corsi.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('abbonatisedute',
    sa.Column('abbonato', sa.Integer(), nullable=False),
    sa.Column('seduta', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['abbonato'], ['abbonati.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['seduta'], ['sedute.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('abbonato', 'seduta')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('abbonatisedute')
    op.drop_table('sedute')
    op.drop_table('prenotazioni')
    op.drop_table('corsislot')
    op.drop_table('salepesislot')
    op.drop_table('nonabbonati')
    op.drop_table('corsi')
    op.drop_table('abbonati')
    op.drop_table('slot')
    op.drop_table('istruttori')
    op.drop_table('clienti')
    op.drop_table('altri')
    op.drop_table('stanze')
    op.drop_table('salepesi')
    op.drop_table('giorni')
    op.drop_table('abbonamenti')
    # ### end Alembic commands ###